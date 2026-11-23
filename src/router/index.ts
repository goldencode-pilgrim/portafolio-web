import Domus from "@/pages/home/domus.vue";
import Pelliculae from "@/pages/pellicula/pelliculae.vue";
import Pellicula from "@/pages/pellicula/pellicula.vue";
import Photographiae from "@/pages/photographia/photographiae.vue";
import Photographia from "@/pages/photographia/photographia.vue";
import Layaout from "@/pages/pictura/Layaout.vue";
import Pictura from "@/pages/pictura/pictura.vue";
import Picturae from "@/pages/pictura/picturae.vue";
import Delineationes from "@/pages/pingo/delineationes.vue";
import Imagines from "@/pages/pingo/imagines.vue";
import LudiciElectronici from "@/pages/ludi electronici/ludi electronici.vue";
import Ludus from "@/pages/ludi electronici/ludus.vue";
import Layaoutludici from "@/pages/ludi electronici/fidesetdesperatioDANA/Layaoutludici.vue";
import DeConsilio from "@/pages/ludi electronici/fidesetdesperatioDANA/de consilio.vue";
import Personae from "@/pages/ludi electronici/fidesetdesperatioDANA/personae.vue";
import Persona from "@/pages/ludi electronici/fidesetdesperatioDANA/persona.vue";
import Maici from "@/pages/maici/maici.vue";
import LayaoutRRSS from "@/pages/rrss/LayaoutRRSS.vue";
import Rrss from "@/pages/rrss/rrss.vue";
import { createRouter, createWebHashHistory } from "vue-router";


export const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),

  routes: [
    {
      path: '/',
      name: 'domus',
      component: Domus,
    },

    {
      path: '/pictura',
      component: Layaout,
      children: [
        {
          path: 'pinacotheca',
          name: 'pinacotheca',
          component: Pictura
        },
        {
          path: 'picturae:id',
          name: 'pinturas',
          component: Picturae
        },
      ]
    },
    {
      path: '/pingo',
      component: Layaout,
      children: [
        {
          path: 'imagines',
          name: 'imagines',
          component: Imagines
        },
        {
          path: 'delineationes:id',
          name: 'delineationes',
          component: Delineationes
        },
      ]
    },                                   
     {
      path: '/photographia',
      component: Layaout,
      children: [
        {
          path: 'pinacotheca',
          name: 'pinacotheca-photo',
          component: Photographiae
        },
        {
          path: 'photographia:id',
          name: 'photographia',
          component: Photographia
        },
      ]
    },                                
    {
      path: '/pelicula',
      component: Layaout,
      children: [
        {
          path: 'pinacotheca',
          name: 'pinacotheca-pelicula',
          component: Pelliculae
        },
        {
          path: 'pelicula:id',
          name: 'pelicula',
          component: Pellicula
        },
      ]
    },                                
    {
      path: '/ludielectronici',
      component: Layaout,
      children: [
        {
          path: '',
          redirect: { name: 'collectione' }
        },
        {
          path: 'collectione',
          name: 'collectione',
          component: LudiciElectronici
        },
        {
          path: 'collectione:id',
          name: 'ludus',
          component: Ludus
        },
        {
          path: 'f&d-dana',
          component: Layaoutludici,
          children: [
            {
              path: '',
              redirect: { name: 'informatio' }
            },
            {
              path: 'informatio',
              name: 'informatio',
              component: DeConsilio
            },
            {
              path: 'personae',
              name: 'personae',
              component: Personae
            },
            {
              path: 'personae:id',
              name: 'persona',
              component: Persona
            },
          ]
        },
      ]
    },
    {
      path: '/maici',
      name: 'maici',
      component: Maici,
    },
    {
      path: '/rrss',
      component: LayaoutRRSS,
      children: [
        {
          path: '',
          name: 'rrss',
          component: Rrss
        },
      ]
    },
    {
      path: '/:patchMatch(.*)',
      redirect: '/'
    }
  ]
})