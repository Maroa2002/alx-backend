import kue from 'kue';
import { createClient } from 'redis';

// Create a Redis client
const redisClient = createClient();

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track job progress: 0%
  job.progress(0, 100);

  // Check if phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  // Track job progress: 50%
  job.progress(50, 100);

  // Simulate sending notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  
  // Mark job as done
  done();
}

// Create a Kue queue
const queue = kue.createQueue({
  redis: {
    createClient: () => redisClient
  }
});

// Process jobs from the queue with a concurrency of 2 jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
