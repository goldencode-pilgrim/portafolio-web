// Datos del "linktree" de la sección RRSS (perfil @gnoseologywithgolden).
export interface Nexus {
  id: number;
  nomen: string;
  url: string;
  /** Descripción que aparece bajo el nombre (opcional) */
  descriptio?: string;
  /** Encabezado de sección previo al enlace (opcional, como en Linktree) */
  caput?: string;
}

export const profilum = {
  nomen: 'Golden the pilgrim',
  titulus: '@gnoseologywithgolden',
  bio: 'Artes visuales 2D 🎨✍🏻 y artes interactivas digitales 🎮 | 🇪🇸 ESP/ENG | ✝️🇻🇦 | Multifandom | WIP',
  citatio: 'Sólo cargar la Cruz nos salvará, no las ideologías.',
};

export const nexus: Nexus[] = [
  { id: 0, nomen: 'Golden the pilgrim', url: 'https://x.com/goldenthpilgrim' },
  {
    id: 1,
    nomen: 'Bluesky',
    url: 'https://bsky.app/profile/goldenpilgrimarts.bsky.social/post/3mw4n6ayjpv2g',
    descriptio: 'Aquí fijaré todos los hilos de la cuenta y procederé a explicar el propósito de la misma.\nEsta cuenta pretende ser el diario de un artista y un llamado a formar comunidad artística por un mundo más santo, uniéndonos para formar compacta milicia por el bien de las almas.\nDios les bendiga.\nAMDG IHS',
  },
  {
    id: 2,
    nomen: 'Mis ensayos.',
    url: 'https://substack.com/@gnoseologiacongolden',
    caput: 'My social network',
    descriptio: 'Ensayos sobre la gran mayoría de ramas del conocimiento, en busca de la defensa de la belleza (amor, poder y logos), CRISTO. Y poesía, pero no afeminada.',
  },
  { id: 3, nomen: 'YouTube', url: 'https://youtube.com/@elgoldenresena1486?sub_confirmation=1' },
  { id: 4, nomen: 'IG', url: 'https://www.instagram.com/goldenarthethics/profilecard/?igsh=MTJobGpqYzQ0cTR2eA==' },
  { id: 5, nomen: 'Mí Odysee', url: 'https://odysee.com/@Gnoseolog%C3%ADaconGolden:8' },
  { id: 6, nomen: 'Game Jolt', url: 'http://gamejolt.com/invite/GoldenResena' },
  { id: 7, nomen: 'Listal', url: 'https://goldencriticas.listal.com/' },
  { id: 8, nomen: 'DeviantArt', url: 'https://www.deviantart.com/gr-artreview' },
];

// URLs extraídas de linktr.ee/goldencriticag. Los enlaces de promoción de la
// propia plataforma Linktree se han omitido a propósito.
