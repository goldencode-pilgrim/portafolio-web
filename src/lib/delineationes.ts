export interface Delineatio {
  id: number;
  titulo: string;
  /** Nombre del archivo dentro de public/imagines/pingo/ */
  imago: string;
}

export const delineationes: Delineatio[] = [
  { id: 0, titulo: 'Delineatio I', imago: 'autoretratoartista2023.jpg' },
  { id: 1, titulo: 'Delineatio II', imago: 'autoretratoartista2023.jpg' },
  { id: 2, titulo: 'Delineatio III', imago: 'autoretratoartista2023.jpg' },
  { id: 3, titulo: 'Delineatio IV', imago: 'autoretratoartista2023.jpg' },
];
