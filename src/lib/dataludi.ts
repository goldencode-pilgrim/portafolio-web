// Datos de los videojuegos de la sección Ludi Electronici.
// El `id` de cada juego genera la URL dinámica:
//   /ludielectronici/collectione0, collectione1, ...
export interface Ludus {
  id: number;
  nomen: string;
  /** Nombre del archivo dentro de public/imagines/videojuegos/ (con extensión) */
  imago: string;
  /** Descripción breve (opcional) */
  descriptio?: string;
}

export const ludi: Ludus[] = [
  {
    id: 0,
    nomen: 'Fides et Desperatio (DANA)',
    imago: 'F&D-DANA-diariodesarrollo1-miniatura.png',
  },
  { id: 1, nomen: 'Polcompass', imago: 'Polcompass.png' },
  { id: 2, nomen: 'Portadas', imago: 'portadasunrojavue.png' },
];

// Añade aquí tus juegos: cada entrada genera automáticamente su imagen
// en el carrusel y su página /ludielectronici/collectione<id>.
