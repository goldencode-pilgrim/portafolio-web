export interface Pictura {
  id: number;
  titulo: string;
  imago: string;
  categoria: string;
  dies: string;
  technica: string;
}

export const picturae: Pictura[] = [
  { id: 0, titulo: 'Autoretrato Artista ', imago: 'pictura 1.jpg', categoria: 'autorretrato', dies: '2024', technica: 'técnica mixta (veladuras de óleo sobre grisalla de acrílico)' },
  { id: 1, titulo: 'Naturaleza surrealista', imago: 'pictura2.jpg', categoria: 'paisaje', dies: '2023', technica: 'técnica mixta (acuarela, acrílico y collage)' },
  { id: 2, titulo: 'La transfigurción de la pintura', imago: 'pictura 3.png', categoria: 'alegoría', dies: '2026', technica: 'óleo sobre lienzo' },
  { id: 3, titulo: 'Caminos de vida', imago: 'pictura 4.png', categoria: 'alegoría', dies: '2026', technica: 'óleo sobre tablas DM' },
];
