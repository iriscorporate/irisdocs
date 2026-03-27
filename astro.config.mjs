import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import react from '@astrojs/react';
import markdoc from '@astrojs/markdoc';
import keystatic from '@keystatic/astro';
import cloudflare from '@astrojs/cloudflare';

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
  
  // You were right! Astro 6 uses static.
  output: 'static',
  adapter: cloudflare(),
  
});