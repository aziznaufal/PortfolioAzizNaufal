from django.shortcuts import render
from .models import Post

from pathlib import Path
import os
from django.shortcuts import render
from django.http import JsonResponse
from .forms import EncryptForm
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature, UnsupportedAlgorithm
import base64


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'encryption/post_list.html', {'posts': posts})

def home(request):
    # posts = Post.objects.all()
    print("masuk sini")
    ##[os.path.join(BASE_DIR, 'templates')]
    print(os.path.join(BASE_DIR, 'templates'))
    return render(request, 'encryption/home.html')


def encrypt_message(request):
    if request.method == 'POST':
        form = EncryptForm(request.POST)
        action = request.POST.get('action')  # Get the action type

        if form.is_valid():
            if action == 'encrypt':
                # Encryption process using the public key
                message = form.cleaned_data['message']
                public_key_text = form.cleaned_data['public_key']
                try:
                    public_key = serialization.load_pem_public_key(
                        public_key_text.encode()
                    )
                    encrypted_message = public_key.encrypt(
                        message.encode(),
                        padding.OAEP(
                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                            algorithm=hashes.SHA256(),
                            label=None
                        )
                    )
                    encrypted_message_b64 = base64.b64encode(encrypted_message).decode('utf-8')
                    return JsonResponse({'encrypted_message': encrypted_message_b64})
                except (ValueError, UnsupportedAlgorithm) as e:
                    return JsonResponse({'error': 'Invalid public key format or unsupported key type for encryption.'})

            elif action == 'decrypt':
                # Decryption process using the private key
                encrypted_message_b64 = form.cleaned_data['encrypted_message']
                private_key_text = form.cleaned_data['private_key']
                try:
                    private_key = serialization.load_pem_private_key(
                        private_key_text.encode(),
                        password=None
                    )
                    encrypted_message = base64.b64decode(encrypted_message_b64)
                    decrypted_message = private_key.decrypt(
                        encrypted_message,
                        padding.OAEP(
                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                            algorithm=hashes.SHA256(),
                            label=None
                        )
                    )
                    return JsonResponse({'decrypted_message': decrypted_message.decode('utf-8')})
                except (ValueError, UnsupportedAlgorithm, Exception) as e:
                    return JsonResponse({'error': 'Invalid private key or message could not be decrypted.'})

    else:
        form = EncryptForm()

    return render(request, 'encryption/encrypt_form.html', {'form': form})


