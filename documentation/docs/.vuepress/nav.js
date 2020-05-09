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
        text: 'Oracle VM Virtual Box (Linux)',
        link: 'https://www.virtualbox.org/wiki/Linux_Downloads'
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
        text: 'ISTD50044.ova (Debian 9.7)',
        link:
          'https://drive.google.com/file/d/1iKXW7YgwMLvZITnJCX8oYDrKlgtouarQ/view?usp=sharing'
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
