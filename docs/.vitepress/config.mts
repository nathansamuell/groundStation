import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "GroundStation",
  description: "Study your rockets with ease",
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
  },
});
