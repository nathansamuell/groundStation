import { defineConfig, type DefaultTheme } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "FlightControl",
  description: "Study your rockets with ease",

  // base url-- https://vitepress.dev/reference/site-config#base
  base: "/flightcontrol/",

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: "/.vitepress/cropped-aiaaweblogo-2.png",

    nav: nav(),

    sidebar: 
      {
        '/user-guide/': { base: '/user-guide/', items: sidebarUser() },
      '/developer-reference/': { base: '/developer-reference/', items: sidebarDev() }
      },

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/nathansamuell/FlightControl",
      },
    ],

    footer: {
      message: "Released under the MIT License",
      copyright: "Copyright © 2024-present Nathan Samuell",
    },
  },
});

function nav(): DefaultTheme.NavItem[] {
  return [
    { text: "About Us", link: "/about/about", activeMatch: "/about/"},
    // { text: "News", link: "/news/news", activeMatch: "/news/"},
    { text: "For Users", link: "/user-guide/user-landing", activeMatch: "/user-guide/" },
    { text: "For Developers", link: "/developer-reference/dev-landing", activeMatch: "/developer-reference/" }
  ]
}

function sidebarUser(): DefaultTheme.SidebarItem[] {
  return [
    {
      text: "Quickstart",
      collapsed: false,
      items: [
        {text: "What is FlightControl?", link:"/user-landing"},
        {text: "Installation", link:"/installation"},
      ]
    },
    {
      text: "Configuring FlightControl",
      collapsed: false,
      items: [
        {text: "Using the .env file", link:"/env?"},
        {text: "Setup", link:"/setup"}
      ]
    }
  ]

}

function sidebarDev(): DefaultTheme.SidebarItem[] {
  return [
    {
      text: "FlightControl Developer Reference",
      collapsed: false,
      items: [
        {text: "Welcome!", link:"/dev-landing"}
      ]
    }
  ]

}
