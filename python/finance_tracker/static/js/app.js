new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    transactions: [],
    newTransaction: {
      description: '',
      amount: '',
      category: ''
    },
    theme: 'light'
  },
  computed: {
    balance() {
      return this.transactions.reduce((total, t) => total + parseFloat(t.amount), 0);
    }
  },
  methods: {
    loadTransactions() {
      fetch('/api/transactions')
        .then(res => res.json())
        .then(data => {
          this.transactions = data;
        })
        .catch(err => console.error('Failed to load transactions:', err));
    },
    addTransaction() {
      if (!this.newTransaction.description || !this.newTransaction.amount || !this.newTransaction.category) {
        alert("All fields are required!");
        return;
      }

      const newTxn = {
        id: Date.now(),
        ...this.newTransaction
      };

      fetch('/api/transactions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newTxn)
      })
        .then(res => {
          if (res.ok) {
            this.transactions.push(newTxn);
            this.newTransaction = { description: '', amount: '', category: '' };
          }
        })
        .catch(err => console.error('Failed to add transaction:', err));
    },
    toggleTheme() {
        console.log("this.theme - ", this.theme);
      this.theme = this.theme === 'light' ? 'dark' : 'light';
      document.body.setAttribute('data-theme', this.theme);
      localStorage.setItem('theme', this.theme);
    },
    initTheme() {
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme) {
        this.theme = savedTheme;
        // document.documentElement.setAttribute('data-theme', savedTheme);
      }
      document.body.setAttribute('data-theme', this.theme);
    }
  },
  created() {
    this.initTheme();
    this.loadTransactions();
  }
});

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/static/js/service-worker.js')
      .then(reg => console.log('Service Worker registered.', reg))
      .catch(err => console.error('Service Worker registration failed:', err));
  });
}

