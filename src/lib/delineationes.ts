export interface Delineatio {
  id: number;
  titulo: string;
  /** Nombre del archivo dentro de public/imagines/pingo/ */
  imago: string;
  categoria: string;
  dies: string;
  technica: string;
}

export const delineationes: Delineatio[] = [
  { id: 0, titulo: 'Práctica modelo 29/10/24', imago: 'delineatione1.jpg', categoria: 'prácticas de clase', dies: '2024', technica: 'carboncillo sobre papel continuo' },
  { id: 1, titulo: 'DB-NB Portada 1', imago: 'delineatione2.jpg', categoria: 'portadas', dies: '2022', technica: 'técnica mixta (acuarela y estilógrafo)' },
];
