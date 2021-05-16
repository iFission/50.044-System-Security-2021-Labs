var nav = require('./nav.js')
var { DownloadsNav, LabsNav } = nav

var utils = require('./utils.js')
var { genNav, getComponentSidebar, deepClone } = utils

module.exports = {
  dest: '../public',
  title: '50.044 Systems Security',
  description: 'LABS',
  base: '/labs/',
  head: [
    [
      'link',
      {
        rel: 'icon',
        href: '/favicon.ico'
      }
    ]
  ],
  themeConfig: {
    repo: 'https://gitlab.com/istd50044/labs/',
    docsRepo: 'https://gitlab.com/istd50044/labs/documentation',
    docsDir: 'docs',
    editLinks: false,
    sidebarDepth: 3,
    search: true,
    searchMaxSuggestions: 10,
    locales: {
      '/': {
        label: 'English',
        selectText: 'Languages',
        editLinkText: 'Edit this page on GitHub',
        nav: [
          {
            text: 'Setup VMs',
            link: '/setup_vm/'
          },
          {
            text: 'Labs Guide',
            items: genNav(deepClone(LabsNav), 'EN')
          },
          {
            text: 'Downloads',
            items: genNav(deepClone(DownloadsNav), 'EN')
          },
          {
            text: 'Questions (Slacker)',
            link: 'https://app.slack.com/client/TNY7NL5V1/CP9N03HDE'
          }
        ],
        sidebar: {
          '/labs/': [
            {
              title: 'Labs Guide',
              collapsable: false,
              children: ['/labs/lab1/', '/labs/lab2/', '/labs/lab3/']
            }
          ],

          '/setup_vm/': [
            {
              title: 'VMs Setup Guide',
              collapsable: false,
              children: ['/setup_vm/']
            }
          ]
        }
      }
    }
  },
  locales: {
    '/': {
      lang: 'en-US',
      description: 'A practical introduction to systems security'
    }
  },
  configureWebpack: {
    resolve: {
      alias: {
        '@public': './public'
      }
    }
  }
}
