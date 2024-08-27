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

// defining the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message'
};

// creating a job in the push_notification_code queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Error creating job:', err);
    } else {
        console.log(`Notification job created: ${job.id}`);
    }
  });

//  Handle job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Handle job failure
job.on('failed', (errorMessage) => {
    console.log('Notification job failed');
})

// Handle job progress
job.on('progress', (progress, data) => {
  console.log(`Notification job ${job.id} is ${progress}% complete`);
});
