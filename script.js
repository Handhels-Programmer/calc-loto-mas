const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.post('/calcular-probabilidad', (req, res) => {
    const combinaciones = req.body.combinaciones;

    // Lógica para calcular la probabilidad (aquí se simplifica para el ejemplo)
    let probabilidad = calcularProbabilidad(combinaciones);

    res.json({ probabilidad });
});

function calcularProbabilidad(combinaciones) {
    // Aquí puedes implementar una lógica más sofisticada
    // por ahora se devolverá una probabilidad fija para cada combinación
    let totalProbabilidad = combinaciones.length * 0.1;  // Ejemplo: 10% de probabilidad por combinación
    return Math.min(totalProbabilidad, 1); // No puede superar el 100%
}

app.listen(PORT, () => {
    console.log(`Servidor corriendo en el puerto ${PORT}`);
});
