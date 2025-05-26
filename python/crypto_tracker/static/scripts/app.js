Vue.config.delimiters = ['[[', ']]'];

new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    coins: [
      { name: "Bitcoin", symbol: "BTCUSDT" },
      { name: "Ethereum", symbol: "ETHUSDT" },
      { name: "Solana", symbol: "SOLUSDT" }
    ],
    searchQuery: '',
    filteredCoins: [],
    selectedCoin: null,
    interval: '1m',
    chartData: [],
    chart: null,
    chartType: 'line',
    searchResults: [],
    livePrice: 0
  },
  methods: {
    searchCoins() {
      if (this.searchQuery.length < 2) {
        this.searchResults = [];
        return;
      }

      fetch(`/api/search?query=${encodeURIComponent(this.searchQuery)}`)
        .then(res => res.json())
        .then(data => {
          this.searchResults = data;
        })
        .catch(err => {
          console.error("Search failed:", err);
        });
    }, selectCoin(coin) {
      this.selectedCoin = coin;
      this.fetchChartData();
      this.fetchLivePrice();
    },
    fetchChartData() {
      if (!this.selectedCoin) return;
      fetch(`/api/kline?symbol=${this.selectedCoin.symbol}&interval=${this.interval}`)
        .then(res => res.json())
        .then(data => {
          this.chartData = data;
          this.renderChart();
        });
    },
    fetchLivePrice() {
      if (!this.selectedCoin) return;
      fetch(`/api/price?symbol=${this.selectedCoin.symbol}`)
        .then(res => res.json())
        .then(data => {
          this.livePrice = parseFloat(data.price).toFixed(2);
        });
    },
    renderChart() {
      const ctx = document.getElementById('priceChart').getContext('2d');
      if (this.chart) this.chart.destroy();

      if (this.chartType === 'line') {
        this.chart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: this.chartData.map(d => new Date(d.x).toLocaleTimeString()),
            datasets: [{
              label: 'Price',
              data: this.chartData.map(d => d.c),
              borderColor: 'blue',
              fill: false
            }]
          }
        });
      } else {
        this.chart = new Chart(ctx, {
          type: 'candlestick',
          data: {
            datasets: [{
              label: 'Candles',
              data: this.chartData
            }]
          }
        });
      }
    }
  },
  computed: {
    filteredCoins() {
      return this.coins.filter(coin =>
        coin.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  watch: {
    selectedCoin() {
      if (this.selectedCoin) {
        clearInterval(this._interval);
        this._interval = setInterval(() => {
          this.fetchLivePrice();
        }, 5000);
      }
    }
  }
});
