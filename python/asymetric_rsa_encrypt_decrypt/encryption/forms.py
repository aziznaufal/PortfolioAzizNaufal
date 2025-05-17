from django import forms

class EncryptForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Message to Encrypt")
    public_key = forms.CharField(widget=forms.Textarea, label="Public Key for Encryption")
    encrypted_message = forms.CharField(widget=forms.Textarea, label="Encrypted Message", required=False)
    private_key = forms.CharField(widget=forms.Textarea, label="Private Key for Decryption", required=False)
