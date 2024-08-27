import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Initialize Express app and Redis client
const app = express();
const client = redis.createClient();

// Promisify Redis functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Array of products
const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Function to get item by id
function getItemById(id) {
    return listProducts.find((product) => product.itemId === id);
}

// Function to reserve stock by id
async function reserveStockById(itemId, stock) {
    await setAsync(`item.${itemId}`, stock);
}

// Function to get current reserved stock by id
async function getCurrentReservedStockById(itemId) {
    const stock = await getAsync(`item.${itemId}`);
    return stock ? parseInt(stock) : null;
}

// Route to get the list of products
app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

// Route to get product details by id
app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);

    if (!product) {
        res.json({ status: 'Product not found' });
        return;
    }

    const currentStock = await getCurrentReservedStockById(itemId);
    const response = {
        ...product,
        currentQuantity: currentStock !== null ? currentStock : product.initialAvailableQuantity
    };
    res.json(response);
});

// Route to reserve a product by id
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);

    if (!product) {
        res.json({ status: 'Product not found' });
        return;
    }

    const currentStock = await getCurrentReservedStockById(itemId);
    const availableStock = currentStock !== null ? currentStock : product.initialAvailableQuantity;

    if (availableStock <= 0) {
        res.json({ status: 'Not enough stock available', itemId });
        return;
    }

    await reserveStockById(itemId, availableStock - 1);
    res.json({ status: 'Reservation confirmed', itemId });
});

// Start the server
app.listen(1245, () => {
    console.log('Server is running on port 1245');
});
