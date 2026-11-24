export interface Pellicula {
  id: number;
  titulo: string;
  /** Archivo de vídeo dentro de public/video/ (ej: 'video1.mp4') */
  video?: string;
  /** Póster opcional dentro de public/imagines/pellicula/ */
  imago?: string;
  categoria: string;
  dies: string;
  technica: string;
}

export const pelliculae: Pellicula[] = [
  { id: 0, titulo: '¿Quién soy? Misión', video: 'video1.mp4', categoria: 'cortometraje', dies: '2024', technica: 'edición de video' },
  { id: 1, titulo: 'El honor ante todo', video: 'video2.mp4', categoria: 'video monataje de fotografías', dies: '2025', technica: 'fotomontaje' },
  { id: 2, titulo: 'Desnudo vers.cut', video: 'video3.mp4', categoria: 'cortometraje', dies: '2024', technica: 'edición de video' },
];

// Cada entrada genera su tesela en la galería y su ficha
// /pelicula/<id> con el vídeo reproduciéndose.
