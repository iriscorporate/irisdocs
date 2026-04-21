import { config, fields, collection } from '@keystatic/core';

export default config({
  storage: {
    kind: 'local',
  },
  collections: {
    // -----------------------------------------------------------
    // IRISOCR SDK v16 Documentation
    // -----------------------------------------------------------
    irisocr_v16: collection({
      label: 'IRISOCR SDK v16',
      slugField: 'title',
      path: 'src/content/docs/16/**',
      format: { contentField: 'content' },
      schema: {
        title: fields.slug({ name: { label: 'Page Title' } }),
        description: fields.text({
          label: 'SEO Description',
          multiline: true,
        }),
        sidebar: fields.object(
          {
            order: fields.integer({
              label: 'Sidebar Order',
              description: 'Lower numbers appear higher in the menu',
              validation: { min: 0 },
            }),
            label: fields.text({
              label: 'Sidebar Label',
              description: 'Override the title in the navigation menu',
            }),
          },
          { label: 'Sidebar Settings' }
        ),
        content: fields.mdx({
          label: 'Content',
          options: {
            image: {
              directory: 'src/assets/images/16',
              publicPath: '@assets/images/16/',
            },
          },
        }),
      },
    }),

    // -----------------------------------------------------------
    // Add future product documentation collections below.
    // Example:
    //
    // my_product: collection({
    //   label: 'My Product Docs',
    //   slugField: 'title',
    //   path: 'src/content/docs/my-product/**',
    //   format: { contentField: 'content' },
    //   schema: { ... },
    // }),
    // -----------------------------------------------------------
  },
});
