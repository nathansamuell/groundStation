import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "GroundStation",
  description: "Study your rockets with ease",

  // base url-- https://vitepress.dev/reference/site-config#base
  base: "/groundStation/",

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: "/cropped-aiaaweblogo-2.png",

    nav: [
      { text: "Home", link: "/" },
      { text: "Examples", link: "/markdown-examples" },
    ],

    sidebar: [
      {
        text: "Examples",
        items: [
          { text: "Markdown Examples", link: "/markdown-examples" },
          { text: "Runtime API Examples", link: "/api-examples" },
        ],
      },
    ],

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/nathansamuell/groundStation",
      },
    ],

    footer: {
      message: "Released under the MIT License",
      copyright: "Copyright © 2024-present Nathan Samuell",
    },
  },
});
