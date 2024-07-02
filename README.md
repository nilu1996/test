+ Vivek & Nilesh


Thank you !!
Chandan Rai
Director of Engineering
Upcoming OOO: Aug 26 to 30

From: Deepak Dobhal <Deepak.Dobhal@amexgbt.com>
Date: Tuesday, July 2, 2024 at 6:46 AM
To: Louisa O'Brien <louisa.obrien@theinformationlab.co.uk>, Neill Rees <Neill.Rees@amexgbt.com>
Cc: Jack de Courcy Robinson <jack@theinformationlab.co.uk>, Andrew Pick <andrew.pick@theinformationlab.co.uk>, Chandan Rai <Chandan@amexgbt.com>, ABHISHEK PARASHAR <ABHISHEK.PARASHAR@amexgbt.com>, hannah.millington@theinformationlab.co.uk <hannah.millington@theinformationlab.co.uk>, Martin Wells <Martin.Wells@amexgbt.com>
Subject: RE: Tableau Server Upgrade - Tuesday 21st May
Hi Neill, Hi Louisa
 
Is there any further update on this? Do we have a date finalized to move forward accounting for CCB approval time and Andy’s availability?
 
I need to inform business users on ETA for server replacement.
 
Regards
Deepak
 
From: Louisa O'Brien <louisa.obrien@theinformationlab.co.uk> 
Sent: Monday, June 24, 2024 7:30 AM
To: Neill Rees <Neill.Rees@amexgbt.com>
Cc: Deepak Dobhal <Deepak.Dobhal@amexgbt.com>; Jack de Courcy Robinson <jack@theinformationlab.co.uk>; Andrew Pick <andrew.pick@theinformationlab.co.uk>; Chandan Rai <Chandan@amexgbt.com>; ABHISHEK PARASHAR <ABHISHEK.PARASHAR@amexgbt.com>; hannah.millington@theinformationlab.co.uk; Martin Wells <Martin.Wells@amexgbt.com>
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hi Neill,
Thanks for explaining that, it does all make sense and it's something that I'll add to our client notes about AMEX - it's a very sensible policy! 
 
Sounds like the best planned time for this would be Andy's time on the 8th July, to make time for these processes to complete - however, would you find it useful to have some of Paul's time tomorrow to help form this proposal to the CCB?
Thanks,
Louisa.
 
On Mon, 24 Jun 2024 at 11:59, Neill Rees <Neill.Rees@amexgbt.com> wrote:
Hi Louisa,
 
Any standard change to a Production environment we must provide a realistic lead time for a change. Usually, when downtime is involved, this is five working days for a Standard change. However, in this instance I would have to submit an Emergency change so we can carry out the reconfiguration urgently but not immediately. Emergency requests are very rare and attract extra scrutiny.
 
The Emergency change would have to have even more structure to the change than a Standard change as the risk is greater. At this point I cannot submit a change as the date has not been agreed, when the downtime will start, when the estimated target is to finish, etc. 
 
All of this takes time to submit, get internal approval(s), and then be submitted to change control. Even then there is no guarantee that they would accept the change request. To get all of this achieved and approved in less than one working day is not something I can control and guarantee. The change control process I cannot bypass or cut short. The ramifications if I attempted to do so on a critical production system I would not risk for a moment.
 
Neill.
 
From: Louisa O'Brien <louisa.obrien@theinformationlab.co.uk> 
Sent: Monday, June 24, 2024 11:39 AM
To: Neill Rees <Neill.Rees@amexgbt.com>
Cc: Deepak Dobhal <Deepak.Dobhal@amexgbt.com>; Jack de Courcy Robinson <jack@theinformationlab.co.uk>; Andrew Pick <andrew.pick@theinformationlab.co.uk>; Chandan Rai <Chandan@amexgbt.com>; ABHISHEK PARASHAR <ABHISHEK.PARASHAR@amexgbt.com>; hannah.millington@theinformationlab.co.uk
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hi Neill,
OK, thanks for the update - do you know what the usual time boundaries of your change control board are/the process to go through, and are you able to share it with us? As noted above, as this is causing production outages we were under the impression this would be looked at as more of support-like problem from the perspective of your IT management.
Thanks,
Louisa.
 
On Mon, 24 Jun 2024 at 11:15, Neill Rees <Neill.Rees@amexgbt.com> wrote:
Hi all,
 
We are now out of time to plan, submit and get change control approval for any work to be carried out tomorrow, it simply would not be accepted. Another date will have to be confirmed.

Further to this I suggest that we remove the downsizing of the cluster from the immediate work for the time being. We should only concentrate on removing the faulty node from the cluster at this time. Otherwise, this introduces too many variables during the reconfiguration. 
 
Once there is confirmation to reduce the cores officially, then we can introduce this change once we have stability with the new, entirely virtual, environment.
 
Thanks,
 
Neill.
 
From: Louisa O'Brien <louisa.obrien@theinformationlab.co.uk> 
Sent: Friday, June 21, 2024 3:43 PM
To: Deepak Dobhal <Deepak.Dobhal@amexgbt.com>
Cc: Jack de Courcy Robinson <jack@theinformationlab.co.uk>; Andrew Pick <andrew.pick@theinformationlab.co.uk>; Neill Rees <Neill.Rees@amexgbt.com>; Chandan Rai <Chandan@amexgbt.com>; ABHISHEK PARASHAR <ABHISHEK.PARASHAR@amexgbt.com>; hannah.millington@theinformationlab.co.uk
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hello all,
Thanks for your patience today. As Jack noted, for some reason we find ourselves in quite a busy period with server work this month so our availability is limited. The best we can do next week is Tuesday with one of our consultants (Paul) who I think some of you will have discussed Alteryx servers with, or alternatively Andy will be available again when he returns on the week of July 8th. 
Neill's outlined what needs to be done (that was really helpful, thank you!) and I'd like to think this could be covered in a day, but re-provisioning a cluster + downsizing it isn't usually the ask in server consultancy, so there is a bit of uncertainty on my part. 
Paul may be able to amend his schedule depending on other work that week but he is currently on site with a client, so I haven't been able to confirm. Would this be amenable to you?
Thanks,
Louisa.
 
 
On Fri, 21 Jun 2024 at 14:03, Deepak Dobhal <Deepak.Dobhal@amexgbt.com> wrote:
Thanks Louisa.
 
While I am sure I made the urgency evident, to further stress it, we are experiencing multiple outages per day – where server is unavailable and then comes back online again in 15 to 30 mins.
 
I am getting this posted on all forums for users. Appreciate the efforts on expediting the support for replacement.
 
Regards
Deepak 
 
From: Louisa O'Brien <louisa.obrien@theinformationlab.co.uk> 
Sent: Friday, June 21, 2024 4:31 AM
To: Jack de Courcy Robinson <jack@theinformationlab.co.uk>
Cc: Deepak Dobhal <Deepak.Dobhal@amexgbt.com>; Andrew Pick <andrew.pick@theinformationlab.co.uk>; Neill Rees <Neill.Rees@amexgbt.com>; Chandan Rai <Chandan@amexgbt.com>; ABHISHEK PARASHAR <ABHISHEK.PARASHAR@amexgbt.com>; hannah.millington@theinformationlab.co.uk
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hello all,
Just to let you know that I've received this and will get back to you with a proposal as soon as I can.
Thanks,
Louisa.
 
On Thu, 20 Jun 2024 at 17:51, Jack de Courcy Robinson <jack@theinformationlab.co.uk> wrote:
Hi Deepak, 
 
Hope you are doing well?
 
Confirming receipt.
 
We did accommodate an effort to upgrade this however an unsupported fallback was in place as advised, which has derailed things. This has been compounded by our team's current availability for a revised date during a very busy period.
 
I am copying our consulting lead Louisa to review if Hannah or a different member(s) of the team with appropriate backup lead support can help here and if so, what availability can be created. 
 
Expectation setting: I am very pessimistic this can be completed prior to the end of June, however we shall try!
 
I'm heading to a wedding tomorrow through Monday. As such, @Louisa, please could you reply if there is a way to make something work early next week? If not, please could I ask if you can secure Andys time for his return in the plan (Liaising with J-mac).
 
Thanks all,
Jack
Jack de Courcy Robinson | Account Director
m:  07939 197252 
 
 
On Thu, 20 Jun 2024 at 16:41, Deepak Dobhal <Deepak.Dobhal@amexgbt.com> wrote:
Hi Jack, Andrew,
 
Hope you are well. 
 
I am reaching out regarding an URGENT issue in Tableau server environment.
 
Our Tableau production environment is facing intermittent hardware failure causing disruption with Tableau server being unavailable. We have critical applications running on this environment with 10s of thousands of users internally as well as client. From Neill, I understand we do not have a schedule available to do a server upgrade for about a month however, we cannot wait that long given the criticality of this application.
 
Can you please get back to us asap on an earlier schedule? Ideally, we would want this upgrade to be done before end of June and preferably during non-business hours.
 
Looking forward to your reply.
 
Regards
Deepak
 
From: Neill Rees <Neill.Rees@amexgbt.com> 
Sent: Thursday, June 20, 2024 11:28 AM
To: Deepak Dobhal <Deepak.Dobhal@amexgbt.com>; Chandan Rai <Chandan@amexgbt.com>; ABHISHEK PARASHAR <ABHISHEK.PARASHAR@amexgbt.com>
Subject: FW: Tableau Server Upgrade - Tuesday 21st May
 
As discussed.
 
From: Andrew Pick <andrew.pick@theinformationlab.co.uk> 
Sent: Friday, June 7, 2024 4:16 PM
To: Neill Rees <Neill.Rees@amexgbt.com>
Cc: Hannah Millington <hannah.millington@theinformationlab.co.uk>; Jack de Courcy Robinson <jack@theinformationlab.co.uk>
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hi Neill, 
 
I am on sabbatical until the 8th July, would anytime after that be ok?
 
Also Jack is off at the minute, he is back on the 17th June, so I presume he will get back to you then.
 
Thanks
 
Andy
 
On Fri, 7 Jun 2024 at 15:16, Neill Rees <Neill.Rees@amexgbt.com> wrote:
Hi Andy,
 
I’m planning to move a share that resides on the same drive where Tableau is installed next weekend, 15th June. This should give me enough space to perform the backup, as Hannah kindly alluded to below. 
 
If that’s successful, then can we pencil something in for later in the month? Can you provide any possible dates from the 24th onwards? I’ll need some lead time to get all the relevant parties on board.
 
One for @Jack de Courcy Robinson, I’ve heard on the grapevine that the idea is that we reduce the number of cores from 32 to 16 for the HRG on-prem instance of Tableau. It’s not been communicated to me internally yet, but is that the case? If so, that’ll be good to know for this reconfiguration exercise.
 
Thanks!
 
Neill.
 
From: Andrew Pick <andrew.pick@theinformationlab.co.uk> 
Sent: Monday, June 3, 2024 9:20 AM
To: Hannah Millington <hannah.millington@theinformationlab.co.uk>
Cc: Neill Rees <Neill.Rees@amexgbt.com>; Jack de Courcy Robinson <jack@theinformationlab.co.uk>
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hi Neill, 
 
Thanks to Hannah for replying while I was off, did you manage to get the backup to work?
 
Thanks
 
Andy
 
On Thu, 30 May 2024 at 09:58, Hannah Millington <hannah.millington@theinformationlab.co.uk> wrote:
Hi Neill,  
 
Andy is on annual leave this week but I can step in here.
 
Writing the backup to a different drive with the tsm command you've quoted should work. 
The only thing to be aware of is that there will still need to be some space on the original disk as during the backup process some data is temporarily stored there. I believe we got up to 90GB free on the original disk after the cleanup we ran last Tuesday which should be enough. 
 
Let me know how it goes and we can look at rescheduling the initial node replacement. 
 
Thanks,
Hannah Millington 
 
On Wed, 29 May 2024 at 15:55, Neill Rees <Neill.Rees@amexgbt.com> wrote:
Hi Andy,
 
I have managed to get a new disk (another 500gb) but I could not extend the current drive as the OS wanted to convert the disk to be a Dynamic disk. This I was not prepared to do as I’m pretty sure that it would wipe out the existing disk, which would make me very unpopular!
 
Instead, I can use this drive as a new standalone drive to meet our initial requirement. From what I’ve read, can the backup be pointed to this drive by using the following command?
 
tsm configuration set -k basefilepath.backuprestore -v "<drive>:\new\directory\path"
 
Would this do the trick? 
 
Cheers,
 
Neill.
 
From: Andrew Pick <andrew.pick@theinformationlab.co.uk> 
Sent: Tuesday, May 21, 2024 11:23 AM
To: Neill Rees <Neill.Rees@amexgbt.com>
Cc: Hannah Millington <hannah.millington@theinformationlab.co.uk>; Jack de Courcy Robinson <jack@theinformationlab.co.uk>
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hi Neill, 
 
Apologies for not being able to complete the required task today however due to the lack of an official Tableau Backup I do not feel comfortable to perform the required changes. I understand you have VM Snapshots available however these are not officially supported by Tableau for backing up the server - link. The reason for the inability to create a backup is due to the lack of available disk space on the server. Despite running maintenance cleanup scripts, we couldn't generate enough space to run a backup. The space required both on the C and D drive can be considerable, further details here.
 
The simplest solution would be to increase the amount of disk space available for node 3, this could even be temporarily made available while performing the backup process. However, while watching the disk space today we did view space decreasing very rapidly on the D drive during an unknown process, this forced us to stop the Tableau Server for a time, to reduce the risk of it being brought down by a lack of disk space. Once stopped, we ran another maintenance cleanup script and this did restore the drive to a previously seen free space amount. This would suggest that there is currently a big risk that the server will have problems due to lack of disk space in the future.
 
Other possibilities/things to consider if increasing disk space is not an option - 
It may be worth us running a Server Health Check to see what is going on with the current server. As you mention, there have been a lot of changes due to the move to the other server so this may highlight a lot of stale content or processes that could be cleaned up.
Alternatively a server admin can view the admin views on Tableau Server and see things such as stale content, this may give a quick insight into any issues
 
 
As a temporary solution you could attempt to run the backup command with the following option - tsm maintenance backup --file <backup_file> --override-disk-space-check. This will try to force the backup to be run, without checking if there is enough space. I don't think this will work but as a last resort to try to get a backup it may be worth trying, however it does run the risk of filling the last remaining space on the drive.
 
I would definitely recommend implementing a housekeeping script that will take ziplogs, run cleanups and take backups on a scheduled basis. We have a script already created that you can apply - https://www.theinformationlab.co.uk/community/blog/updated-tableau-server-housekeeping-made-easy-windows-edition/
 
If you have any other questions please let me know,
 
Thanks
 
Andy
 
 
 
 
 
 
On Mon, 20 May 2024 at 15:07, Neill Rees <Neill.Rees@amexgbt.com> wrote:
Hi Andy,
 
I’ll be up super early as two of my five cats will wake me without question! I’ll do a backup then so it’ll be really fresh. 
 
Invite on the way to you both, also.
 
Cheers,
 
Neill.
 
From: Andrew Pick <andrew.pick@theinformationlab.co.uk> 
Sent: Monday, May 20, 2024 10:51 AM
To: Neill Rees <Neill.Rees@amexgbt.com>
Cc: Hannah Millington <hannah.millington@theinformationlab.co.uk>
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hi Neil, 
 
I am not sure how often you take backups? If not already scheduled, would it be possible to take one this evening? We then won't have to take time out tomorrow to create one.
 
Official steps here if needed - https://help.tableau.com/current/server/en-us/backup_restore.htm#backing-up-tableau-server-for-recovery
 
Cheers
 
Andy
 
On Fri, 17 May 2024 at 11:54, Neill Rees <Neill.Rees@amexgbt.com> wrote:
Hi Andy,
 
Yes, I’ve still got that from the one of the other nodes, so we’re all good.
 
 
From: Andrew Pick <andrew.pick@theinformationlab.co.uk> 
Sent: Friday, May 17, 2024 11:53 AM
To: Neill Rees <Neill.Rees@amexgbt.com>
Cc: Hannah Millington <hannah.millington@theinformationlab.co.uk>
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hi Neill, 
 
Sorry, one more thing, I have just checked and the installation file for 2022.3.0 is no longer available - https://www.tableau.com/support/releases/server/2022.3
Do you have it available? The closest one still available to download is 2022.3.15. But that would require upgrading all the other nodes.
 
Thanks
 
Andy
 
On Fri, 17 May 2024 at 11:44, Neill Rees <Neill.Rees@amexgbt.com> wrote:
It’s Windows.
 
From: Andrew Pick <andrew.pick@theinformationlab.co.uk> 
Sent: Friday, May 17, 2024 11:44 AM
To: Neill Rees <Neill.Rees@amexgbt.com>
Cc: Hannah Millington <hannah.millington@theinformationlab.co.uk>
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
HI Neill, 
 
Thanks for confirming, one more question, are you on Windows or Linux?
 
Cheers
 
Andy
 
On Fri, 17 May 2024 at 11:39, Neill Rees <Neill.Rees@amexgbt.com> wrote:
Hi Andy,
 
Yes, exactly that – no upgrade, just a move of the processes as you see fit to the new node or the existing nodes, if necessary, but I’d assume you would be carrying out a ‘lift and shift’.
 
I’ll send out the meeting request shortly.
 
Cheers,
 
Neill.
 
 
 
From: Andrew Pick <andrew.pick@theinformationlab.co.uk> 
Sent: Friday, May 17, 2024 11:04 AM
To: Neill Rees <Neill.Rees@amexgbt.com>
Cc: Hannah Millington <hannah.millington@theinformationlab.co.uk>
Subject: Re: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hi Neill, 
 
That all makes sense. Just to confirm, this is just replacing a node, not upgrading or making any other configuration changes?
 
Happy to start at 8 on Tuesday. I am busy from 14:30 on Tuesday so if we haven't finished Hannah will still be on the call.
 
Thanks
 
Andy
 
On Thu, 16 May 2024 at 16:53, Neill Rees <Neill.Rees@amexgbt.com> wrote:
Hi both,
 
So, the scenario we have here is that we have a three-node quorum. Maverick is on its last legs and often just cuts out for no apparent reason on an almost daily basis. As Maverick is an aged physical server, we need to remove from the equation as when it goes dark, so does Tableau as a whole. 
 
I have provisioned a new server (OL3TABLEAU03, not listed below) which I am finalising the details of as we speak, but I hope to have everything in place by Tuesday. In essence, it should be the same in terms of hardware and disk as Maverick.
 
In short, we need to transfer all processes from Maverick to OL3TABLEAU03. From memory of the previous exercise, we carried out this exercise (ironically, to make Maverick the main node), we installed Tableau on the new servers, OL3TABLEAU01 and OL3TABLEAU02, and then processes were moved back to Maverick. For info, OL3TABLEAU01 and 02 are of a lower spec than Maverick, so that may explain why some processes are where they are – I’m no Tableau expert by any means, I basically just keep the thing up!
 
For Tuesday, I believe what you folks will need to do, with me giving you control, is to install Tableau version 2022.3.0 (as per the existing instances), bootstrap to the quorum and then reconfigure the services accordingly. By then, I hope to have all the networking sorted out by then so that OL3TABLEAU03 can communicate with the outside world and do everything that Maverick currently does and be the public facing Tableau server.
 
I think that’s it in a nutshell, but if you have any questions before Tuesday, please let me know. I’d like to start at 8am on Tuesday if that’s agreeable with you both. This is to alleviate any angst from our folks in the US if we drift into their waking hours. From the previous event, I believe we were finished by around 11.30am.
 
I cannot thank you enough for picking this up at such short notice. It’s truly appreciated.
 
 
 
Regards,
 
Neill.
 
From: Jack de Courcy Robinson <jack@theinformationlab.co.uk> 
Sent: Thursday, May 16, 2024 4:27 PM
To: Neill Rees <Neill.Rees@amexgbt.com>
Cc: Andrew Pick <andrew.pick@theinformationlab.co.uk>; Hannah Millington <hannah.millington@theinformationlab.co.uk>
Subject: Tableau Server Upgrade - Tuesday 21st May
 
CAUTION: This email originated from outside the organization. Do not click links or open attachments unless you recognize the sender and expect that the content is safe.
Hi Neill, 
 
Please be introduced to Andrew and Hannah, who will be working with you next Tuesday. If you would kindly share any further you think may be helpful in advance, that will help support the success of the day.
 
I will leave you to organise timings etc with Andrew and Hannah directly if thats ok.

 
Many thanks,
Jack
 
Check out upcoming events.
Jack de Courcy Robinson | Account Director
m:  07939 197252 
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________


 
-- 
Hannah Millington
The Information Lab
e
hannah.millington@theinformationlab.co.uk
w
www.theinformationlab.co.uk

 
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________


-- 
 
Louisa O'Brien
The Information Lab
e
louisa.obrien@theinformationlab.co.uk
| m
a
w
www.theinformationlab.co.uk
   

 
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________


-- 
 
Louisa O'Brien
The Information Lab
e
louisa.obrien@theinformationlab.co.uk
| m
a
w
www.theinformationlab.co.uk
   

 
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________


-- 
 
Louisa O'Brien
The Information Lab
e
louisa.obrien@theinformationlab.co.uk
| m
a
w
www.theinformationlab.co.uk
   

 
 
________________________________________
Notice: GBT Travel Services UK Limited (GBT UK) and its authorised sublicensees (including Ovation Travel Group and Egencia) use certain trademarks and service marks of American Express Company or its subsidiaries (American Express) in the 'American Express Global Business Travel' and 'American Express GBT Meetings & Events' brands and in connection with its business for permitted uses only under a limited licence from American Express (Licensed Marks). The Licensed Marks are trademarks or service marks of, and the property of, American Express. GBT UK is a subsidiary of Global Business Travel Group, Inc. (NYSE: GBTG). American Express holds a minority interest in GBTG, which operates as a separate company from American Express.
________________________________________
This email message and all attachments transmitted with it are solely for the use of the intended recipient(s) and may contain confidential and/or privileged information. If the reader of this message is not the intended recipient, you are hereby notified that any dissemination, distribution, copying and/or other use of this message or its attachments is strictly prohibited. If you have received this message in error, please notify the sender and delete it immediately. Unintended transmission shall not constitute a waiver of the attorney-client or any other privilege.
________________________________________
Avis : GBT Travel Services UK Limited (GBT UK) et ses détenteurs de sous-licence autorisés (notamment Ovation Travel Group et Egencia) utilise certaines marques commerciales et marques de services d’American Express Company ou de ses filiales (American Express) dans les marques « American Express Global Business Travel » et « American Express GBT Meetings & Events » ainsi qu’en lien avec son activité, à des fins autorisées uniquement, sous une licence limitée accordée par American Express (marques sous licence). Les marques sous licence sont des marques commerciales ou des marques de services d’American Express, dont elles sont la propriété. GBT UK est une filiale de Global Business Travel Group, Inc. (NYSE : GBTG). American Express détient une participation minoritaire dans GBTG, qui opère en tant que société distincte d’American Express. 
________________________________________
Ce message électronique et toutes les pièces jointes transmises avec celui-ci sont uniquement destinés à l’usage du ou des destinataires visés et peuvent contenir des informations confidentielles et/ou privilégiées. Si le lecteur de ce message n’est pas le destinataire prévu, vous êtes informé par la présente que toute diffusion, distribution, copie et/ou autre utilisation de ce message ou de ses pièces jointes est strictement interdite. Si vous avez reçu ce message par erreur, veuillez en informer l’expéditeur et le supprimer immédiatement. Une transmission involontaire ne constitue pas une renonciation au secret professionnel ou à toute autre prérogative.
________________________________________
Aviso: GBT Travel Services UK Limited (GBT UK) y sus sublicenciatarios autorizados (incluyendo Ovation Travel Group y Egencia) utilizan ciertas marcas registradas y marcas de servicio de American Express Company o sus filiales (American Express) en las marcas «American Express Global Business Travel» y «American Express GBT Meetings & Events» y en relación con su negocio, solo para usos autorizados, bajo una licencia limitada de American Express (marcas bajo licencia). Las marcas bajo licencia son marcas registradas o marcas de servicio de American Express, de quien son propiedad. GBT UK es una filial de Global Business Travel Group, Inc. (NYSE: GBTG). American Express tiene participación minoritaria en GBTG, que opera como empresa independiente de American Express.
________________________________________
Este mensaje de correo electrónico y sus archivos adjuntos son para el uso exclusivo de los destinatarios y pueden contener información confidencial o privada. Si usted no es el destinatario previsto, se le notifica que está terminantemente prohibido difundir, distribuir, copiar o dar otros usos a este mensaje o sus archivos adjuntos. Si ha recibido este mensaje por error, por favor notifique al remitente y elimínelo inmediatamente. El envío accidental no constituirá una renuncia a los privilegios de abogado-cliente ni a ningún otro privilegio.
________________________________________


-- 
 
Louisa O'Brien
The Information Lab
e
louisa.obrien@theinformationlab.co.uk
| m
a
w
www.theinformationlab.co.uk
   

 
