var DownloadsNav = [
  {
    textEN: 'Required Software',
    items: [
      {
        text: 'Oracle VM Virtual Box (Windows)',
        link:
          'https://download.virtualbox.org/virtualbox/6.1.6/VirtualBox-6.1.6-137129-Win.exe'
      },
      {
        text: 'Oracle VM Virtual Box (MAC OS)',
        link:
          'https://download.virtualbox.org/virtualbox/6.1.6/VirtualBox-6.1.6-137129-OSX.dmg'
      },
      {
        text: 'MobaXterm (SSH Client for Windows)',
        link: 'https://mobaxterm.mobatek.net/download-home-edition.html'
      }
    ]
  },
  {
    textEN: 'Virtual Machine',
    items: [
      {
        text: 'Debian VM (Oracle Virtual Box)',
        link: 'https://github.com/PanJiaChen/vue-element-admin'
      }
    ]
  }
]

var LabsNav = [
  {
    text: 'Labs Selection',
    items: [
      {
        text: 'Lab 1 - Memory vulnerabilities',
        link: '/labs/lab1/'
      },
      {
        text: 'Lab 2 - Privilege separation',
        link: '/labs/lab2/'
      },
      {
        text: 'Lab 3 - Web security',
        link: '/labs/lab3/'
      }
    ]
  }
]

module.exports = {
  DownloadsNav,
  LabsNav
}
