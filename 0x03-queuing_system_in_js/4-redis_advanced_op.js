import { createClient, print } from "redis";

// create a redis client
const client = createClient();

// Connect to the Redis Server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// function to create a harsh
function createHolbertonSchoolsHash() {
  client.hset('HolbertonSchools', 'Portland', 50, print);
  client.hset('HolbertonSchools', 'Seattle', 80, print);
  client.hset('HolbertonSchools', 'New York', 20, print);
  client.hset('HolbertonSchools', 'Bogota', 20, print);
  client.hset('HolbertonSchools', 'Cali', 40, print);
  client.hset('HolbertonSchools', 'Paris', 2, print);
}

// function to display the hash stored in Redis
function displayHolbertonSchoolsHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
        console.error(`Error retrieving hash: ${err.message}`);
    } else {
        console.log(reply);
    }
  });
}

createHolbertonSchoolsHash();
displayHolbertonSchoolsHash();
