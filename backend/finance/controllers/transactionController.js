
// controllers/transactionController.js
const db = require('../database/postgres/client');

exports.purchaseAddon = async (req, res) => {
    const { userId, addonId, price } = req.body;
    
    try {
        // بدء عملية الربط (Transaction)
        await db.query('BEGIN');
        
        // 1. خصم الرصيد
        const user = await db.query('UPDATE users SET wallet = wallet - $1 WHERE id = $2', [price, userId]);
        
        // 2. تسجيل العملية
        await db.query('INSERT INTO transactions (user_id, amount, type) VALUES ($1, $2, $3)', [userId, price, 'STORE_PURCHASE']);
        
        await db.query('COMMIT');
        res.status(200).json({ message: "تمت العملية بنجاح" });
        
    } catch (error) {
        await db.query('ROLLBACK');
        res.status(500).json({ error: "فشل الربط البرمجي" });
    }
};
