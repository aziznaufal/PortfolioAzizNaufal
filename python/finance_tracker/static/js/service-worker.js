const CACHE_NAME = 'finance-tracker-cache-v1';
const urlsToCache = [
  '/',
  '/static/js/app.js',
  '/static/css/style.css',
  '/static/manifest/manifest.json',
  'https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js',
  // add any other assets here you want cached
  '/static/icons/icon-192x192.png',
  '/static/icons/icon-512x512.png'
];

// Install + cache files
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Clean up old caches on activate
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keyList => {
      return Promise.all(
        keyList.map(key => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    })
  );
});

// Fetch from cache first, then network
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
