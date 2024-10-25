---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "GroundStation"
  text: "Rocket Monitoring Reimagined 🚀"
  tagline: Developed by Nathan Samuell for AIAA-UH
  actions:
    - theme: brand
      text: Get Started
      link: /markdown-examples
    - theme: alt
      text: In The Wild
      link:
    - theme: alt
      text: GitHub
      link: https://github.com/nathansamuell/groundStation

features:
  - title: Real-Time monitoring
    details: View formatted and processed data in real-time from your rocket
  - title: Visuals
    details: IN PROGRESS
  - title: No file corruptions
    details: Flight data is saved to backup files to prevent data loss in the event of power loss or app failure
  - title: APRS Broadcasting
    details: Share your rocket's status with spectators around the world
---




<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [
  {
    avatar: 'https://www.github.com/nathansamuell.png',
    name: 'Nathan Samuell',
    title: 'Creator',
    links: [
      { icon: 'github', link: 'https://github.com/nathansamuell' },
      { icon: 'linkedin', link: 'https://linkedin.com/in/nathan-samuell' }
    ]
  },

  {
    avatar: 'https://www.github.com/shriy97.png',
    name: 'Shriyans Sai',
    title: 'Developer',
    links: [
      { icon: 'github', link: 'https://github.com/shriy97' },
      { icon: 'linkedin', link: 'https://linkedin.com/in/shriyans-sai' }
    ]
  },

  {
    avatar: 'https://www.github.com/lulusartajmd.png',
    name: 'Lulu Sartaj Mohammad',
    title: 'Devloper',
    links: [
      { icon: 'github', link: 'https://github.com/lulusartajmd' },
      { icon: 'linkedin', link: 'https://linkedin.com/in/lulu-sartaj-mohammad/' }
    ]
  },

  {
    avatar: 'https://www.github.com/UH-AIAA.png',
    name: 'AIAA UH',
    title: 'Affiliate',
    links: [
      { icon: 'github', link: 'https://github.com/UH-AIAA' }
    ]
  }
]
</script>




# Our Team

Say hello to our awesome team.

<VPTeamMembers size="small" :members="members" />
