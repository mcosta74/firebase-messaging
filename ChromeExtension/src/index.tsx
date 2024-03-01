/// <reference lib="webworker" />

import { initializeApp } from "firebase/app";
import { getMessaging, onBackgroundMessage } from "firebase/messaging/sw";
import { getToken } from "firebase/messaging";

declare const self: ServiceWorkerGlobalScope;

const firebaseConfig = {
  // past here your Firebase app config
};

initializeApp(firebaseConfig);

chrome.runtime.onInstalled.addListener(async () => {
  const token = await getToken(getMessaging(), {
    serviceWorkerRegistration: self.registration,
  });
  console.log('FCM token:', token);
});

onBackgroundMessage(getMessaging(), (payload) => {
  console.log('Message received:', payload);
});
