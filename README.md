We are currently experiencing a potential port conflict issue on our EC2 instance, where an application is already running on ports 443 and 8383. The application operates as a service and does not require a web browser for access.

The challenge arises from the need to set up a new RMT (Remote Management Tool) master server on the same EC2 instance. The RMT setup requires the use of ports 443 and 5672. Given that port 443 is already in use by the existing application, I am concerned that this new setup might lead to a conflict, potentially disrupting the current service.

To address this issue, I seek your guidance on possible alternatives or solutions that would allow both the existing application and the new RMT master server to coexist without any conflicts.

Would it be advisable to:

Reassign the RMT master server to use alternative ports if feasible?
Consider setting up a reverse proxy or load balancer to manage traffic across the conflicting ports?
Explore the possibility of migrating one of the services to a different EC2 instance to avoid port overlap?
Your expertise on this matter would be greatly appreciated as we work towards a solution that ensures the stability and continuity of both services.
