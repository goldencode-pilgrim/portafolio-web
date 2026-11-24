export interface Photographia {
  id: number;
  titulo: string;
  imago: string;
  categoria: string;
  dies: string;
  technica: string;
}

export const photographiae: Photographia[] = [
  { id: 0, titulo: 'Photographia I', imago: 'photo1.jpg', categoria: 'maqueta', dies: '2025', technica: 'maqueta y fotografía editada' },
  { id: 1, titulo: 'Photographia II', imago: 'photo2.jpg', categoria: 'alegoría', dies: '2025', technica: 'fotografía editada tiempos de exposición largos' },
  { id: 2, titulo: 'Dualidad', imago: 'photo3.JPG', categoria: 'alegoría', dies: '2025', technica: 'fotografía editada tiempos de exposición largos' },
 
];
