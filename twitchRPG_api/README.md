# API Routes

| URL                                   | Params                     | Type   |
| ------------------------------------- |:-------------------------- |:------:|
|  /                                    |                            |  GET   |
|  /channels                            |                            |  GET   |
|  /channels/:id                        |  channel_id                |  GET   |
|  /channels/status                     |                            |  PUT   |
|  /facebook/checkaccount/:id           |  fb_account                |  GET   |
|  /facebook/checkcampaign/:id1/:id2    |  fb_account, fb_campaign   |  GET   |
|  /adwords/checkaccount/:id            |  adw_account               |  GET   |
|  /adwords/checkcampaign/:id1/:id2     |  adw_account, adw_campaign |  GET   |
|  /analytics/checkaccount/:id          |  ga_account                |  GET   |
|  /analytics/checkprofile/:id          |  ga_profile                |  GET   |
|  /analytics/trackingevent/:id         |  ga_profile                |  GET   |
|  /chromaprint/search                  |                            |  POST  |
|                                       |                            |        |
