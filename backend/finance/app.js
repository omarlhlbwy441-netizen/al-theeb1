
const express = require('express');
const app = express();
app.use(express.json());

// 1. نظام المالية
app.post('/deposit', (req, res) => {
    res.json({ message: "تم إيداع الرصيد بنجاح" });
});

// 2. نظام المتجر والإضافات
app.post('/purchase_addon', (req, res) => {
    const { userId, addonId } = req.body;
    // منطق خصم الرصيد وتفعيل الإضافة في الحاوية
    res.json({ message: "تم شراء الإضافة وتفعيلها في مشروعك" });
});

// 3. نظام إدارة المشاريع والحاويات
app.post('/create_container', (req, res) => {
    res.json({ message: "تم إنشاء حاوية المشروع بنجاح" });
});

app.listen(3001, () => {
    console.log("Wolf Node.js Services Running on port 3001");
});
