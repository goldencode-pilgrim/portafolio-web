// Datos de los personajes de "Fides et Desperatio" (DANA).
// El `id` de cada personaje es el que aparece en la URL dinámica:
//   /ludielectronici/f&d-dana/personae0, personae1, ...
export interface Persona {
  id: number;
  nomen: string;
  /** Nombre del archivo dentro de public/imagines/ludici/ (opcional) */
  imago?: string;
  /** Descripción del personaje (opcional) */
  descriptione?: string;
  /** Cita característica (opcional) */
  citatio?: string;
}

export const personae: Persona[] = [
  { id: 0, nomen: 'Dana' },
  { id: 1, nomen: 'Fides' },
  { id: 2, nomen: 'Desperatio' },
  { id: 3, nomen: 'Spes' },
];

// Esquema básico sin datos reales todavía: añade `imago`, `descriptione`
// y `citatio` cuando los tengas. Las imágenes irán en public/imagines/ludici/.
// (Los nombres son provisionales, tomados del título del juego.)
