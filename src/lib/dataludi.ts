// Datos de los videojuegos de la sección Ludi Electronici.
// Cada juego enlaza a su `ruta` desde el carrusel (por defecto '/')
export interface Ludus {
  id: number;
  nomen: string;
  /** Nombre del archivo dentro de public/imagines/videojuegos/ (con extensión) */
  imago: string;
  /** Ruta a la que navega el clic en su imagen (si no se define: '/') */
  ruta?: string;
  /** Descripción breve (opcional) */
  descriptio?: string;
  categoria: string;
  dies: string;
  status: string;
  video: string;
}

export const ludi: Ludus[] = [
  {
    id: 0,
    nomen: 'Fides et Desperatio (DANA)',
    imago: 'F&D-DANA-diariodesarrollo1-miniatura.png',
    ruta: '/ludielectronici/0',
    categoria: 'JRPG y survival horror.',
    dies: '2026-',
    status: 'WIP',
    video:'',
  },
  { id: 1, nomen: 'Polcompass', imago: 'Polcompass.png', ruta: '/ludielectronici/1', categoria: '', dies: '', technica: '' },
  { id: 2, nomen: 'Portadas', imago: 'portadasunrojavue.png', ruta: '/ludielectronici/2', categoria: '', dies: '', technica: '' },
];

// Las rutas /ludielectronici/0, /1 y /2 están en el router:
// 0 → de consilio (F&D-DANA), 1 → deconsiliopolcompball, 2 → deconsilios&l.
