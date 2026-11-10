const express = require('express');
const cors = require('cors');
const { Pool } = require('pg');
require('dotenv').config();

const app = express();
app.use(express.json());
app.use(cors());

// Conexión a la base de datos PostgreSQL de Supabase
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

// Ruta de prueba para verificar que el servidor está activo
app.get('/', (req, res) => {
  res.json({ status: 'Servidor ERDO funcionando al 100%' });
});

// Ruta para obtener los niveles VIP
app.get('/api/vip-levels', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM vip_levels ORDER BY level ASC');
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error al obtener los niveles VIP' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});
