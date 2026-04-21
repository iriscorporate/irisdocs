import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import react from '@astrojs/react';
import markdoc from '@astrojs/markdoc';
import keystatic from '@keystatic/astro';

export default defineConfig({
  integrations: [
    starlight({
      title: 'IRISOCR™ SDK Documentation',
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        {
          label: 'Version 16 Documentation',
          autogenerate: { directory: '16' },
        },
      ],
    }),
    react(),
    markdoc(),
    keystatic(),
  ],

  output: 'static',
});