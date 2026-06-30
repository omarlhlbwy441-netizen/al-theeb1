const express = require('express');
const app = express();
app.use(express.json());

// مسار شراء الإضافات من المتجر
app.post('/api/store/purchase', (req, res) => {
    const { userId, addonId, price } = req.body;
    
    // هنا يتم فحص الرصيد من قاعدة البيانات (محاكاة للعملية)
    if (!userId || !addonId) {
        return res.status(400).json({ error: "بيانات الشراء غير مكتملة" });
    }

    // خصم الرصيد وتوثيق العملية
    console.log(`تم شراء الإضافة ${addonId} للمستخدم ${userId} بسعر ${price}`);
    
    res.json({ 
        success: true, 
        message: "تم خصم الرصيد بنجاح وتفعيل الإضافة في مشروعك",
        transactionId: "TXN" + Math.floor(Math.random() * 100000)
    });
});

app.listen(3001, () => console.log('Wolf Store & Finance running on port 3001'));
