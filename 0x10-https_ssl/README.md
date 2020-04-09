## 0x10. HTTPS SSL
---

### Task
---
0. HTTPS ABC 
1. World wide web
2. HAproxy SSL termination
3. No loophole in your website traffic 

### Description
---
0. What is HTTPS? Why do you need HTTPS? You want to setup HTTPS on your website, where shall you place the certificate?
1. Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.
2. Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..
3. A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.
