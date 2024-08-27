import kue from 'kue';
import { createClient } from 'redis';

// creating a redis client
const redisClient = createClient();

// creating a Kue queue
const queue = kue.createQueue({
  redis: {
    createClient: () => redisClient
  }
});

// function to send notifications
function sendNotification(phoneNumber, message) {
  console.log(`Sending notifiation to ${phoneNumber}, with message: ${message}`);
}

// process jobs in the queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message} = job.data;
  sendNotification(phoneNumber, message);
  done();
});
