import kue from 'kue';

export default function createPushNotificationsJobs(jobs, queue) {
    // Check if the jobs argument is an array
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    // Iterate over each job in the jobs array
    jobs.forEach((jobData) => {
        // Create a job in the queue push_notification_code_3
        const job = queue.create('push_notification_code_3', jobData);

        // Log when the job is created
        job.on('enqueue', () => {
            console.log(`Notification job created: ${job.id}`);
        })
        .on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        })
        .on('failed', (error) => {
            console.log(`Notification job ${job.id} failed: ${error}`);
        })
        .on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });

        // Save the job to the queue
        job.save();
    });
}
