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




# About Us

GroundStation started as Nathan's solo project for AIAA-UH to perform some menial rocket monitoring tasks. It has since expanded into a comprehensive application in its own right, developed and engineered by the Avionics Team @ AIAA-UH!


## Say Hello to the Dev Team!

<VPTeamMembers size="small" :members="members" />