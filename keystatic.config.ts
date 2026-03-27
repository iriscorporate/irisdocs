// keystatic.config.ts
import { config, fields, collection } from '@keystatic/core';

export default config({
  storage: {
    kind: 'local',
  },
  collections: {
    // -----------------------------------------------------------
    // Version 16.3 Documentation
    // -----------------------------------------------------------
    v16_3: collection({
      label: 'v16.3 Documentation',
      slugField: 'title', // <--- CHANGED BACK TO TITLE
      path: 'src/content/docs/16.3/*',
      format: { contentField: 'content' },
      schema: {
        // We name this 'title' so Starlight is happy
        title: fields.slug({ name: { label: 'Page Title' } }),
        
        description: fields.text({ 
          label: 'SEO Description', 
          multiline: true 
        }),
        
        // Sidebar Settings (With the fix from before)
        sidebar: fields.object(
          {
            order: fields.integer({ 
              label: 'Sidebar Order',
              description: 'Lower numbers appear higher in the menu',
              validation: { min: 0 } 
            }),
            label: fields.text({ 
              label: 'Sidebar Label',
              description: 'Override the title in the navigation menu' 
            }),
          },
          {
            label: 'Sidebar Settings' // Options as second argument
          }
        ),

        content: fields.mdx({
          label: 'Content',
          options: {
            image: {
              directory: 'src/assets/images/16.3',
              publicPath: '@assets/images/16.3/',
            }
          }
        }),
      },
    }),

    // -----------------------------------------------------------
    // Version 16.2 Documentation (LTS)
    // -----------------------------------------------------------
    v16_2: collection({
      label: 'v16.2 (LTS)',
      slugField: 'title', // <--- CHANGED BACK TO TITLE
      path: 'src/content/docs/16.2/*',
      format: { contentField: 'content' },
      schema: {
        title: fields.slug({ name: { label: 'Page Title' } }),
        description: fields.text({ label: 'SEO Description', multiline: true }),
        
        sidebar: fields.object(
          {
            order: fields.integer({ label: 'Order', validation: { min: 0 } }),
            label: fields.text({ label: 'Label' }),
          },
          {
            label: 'Sidebar Settings'
          }
        ),

        content: fields.mdx({
          label: 'Content',
          options: {
            image: {
              directory: 'src/assets/images/16.2',
              publicPath: '@assets/images/16.2/',
            }
          }
        }),
      },
    }),
  },
});