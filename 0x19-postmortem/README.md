![image](https://github.com/sarodcreator/alx-system_engineering-devops/assets/105171880/8ab1bdad-6c28-4cbc-9663-a166df3f459e)

### Summary

From 6:00 AM to 7:50 PM GMT, requests to the Holberton API, hosted on the 0x17-web_stack_debugging_3 sandbox, resulted in 500 error responses. This caused applications relying on the API to malfunction or display errors. The incident reached a point where it affected all traffic to this API. The outage was traced back to a typographical error in the configuration files, causing the API to fail.

### Timeline (GMT)
- **5:45 AM**: Configuration update begins
- **5:46 AM**: Outage starts
- **6:00 AM**: Monitoring systems alert teams (ALX releases 0x17-web_stack_debugging_3)
- **7:30 PM**: Apache2 status checked (running)
- **7:40 PM**: PHP configuration files inspected and wp-settings.php corrected
- **7:49 PM**: Server restarts initiated
- **7:50 PM**: Full traffic restored

### Root Cause & Resolution

#### Root Cause
At 5:45 AM GMT, a configuration change containing a typo (".phpp" instead of ".php") in wp-settings.php was mistakenly pushed directly to production. This error caused Apache to return 500 errors for PHP requests, leading to thread consumption and queuing traffic. The servers began hanging and restarting, resulting in an outage at 5:46 AM GMT.

#### Resolution
By 6:00 AM GMT, monitoring systems had alerted the engineering team, who began investigating. By 7:40 PM, they discovered the typo exacerbated by the monitoring system. Attempts to restart Apache2 at 7:30 PM confirmed it was running, prompting a deeper investigation using ltrace, which identified the typo. Given the size of the configuration file, a Puppet script was used to correct the error throughout. Gradual job recovery began, and by 7:49 PM, 90% of traffic was restored. Full restoration was achieved by 7:50 PM.

### Corrective & Preventive Measures
Following an internal review, the following measures will be implemented to prevent similar issues:

- Disable the current configuration release process until safer alternatives are in place.
- Develop a faster and more reliable rollback procedure.
- Ensure all configuration typos are fixed prior to deployment.
- Enforce staged rollouts of configuration changes programmatically.
- Enhance auditing processes for high-risk configuration options.

ALX remains dedicated to improving our technological and operational practices to prevent outages. We appreciate your patience and apologize for the inconvenience caused to you, your users, and your organization. Thank you for your continued support and trust.
