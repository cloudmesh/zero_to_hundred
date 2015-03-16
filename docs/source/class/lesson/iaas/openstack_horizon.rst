OpenStack Web Dashboard (Horizon)
===============================================================================

On FutureSystems, we have a web interface for OpenStack cloud management,
OpenStack Horizon. It supports most functionality that you can use to manage
cloud resources via commannd line tools such as Nova Compute CLI with graphical
illustration.

Overview
-------------------------------------------------------------------------------

OpenStack Horizon is a GUI for managing OpenStack cloud. It is mainly developed
by a open source web application framework, Django and Python. Some of the
JavasScript and CSS libraries are also included such as, jQuery, AngularJS, D3,
Font-Awesome, Jasmine, Qunit, Rickshaw, etc.

Source code of Horizon (GitHub)
-------------------------------------------------------------------------------

GitHub: https://github.com/openstack/horizon

Horizon on FutureSystems
-------------------------------------------------------------------------------

.. list-table:: Horizon endpoints
   :header-rows: 1
   :widths: 10,10,10,10,30

   * - Image
     - Version
     - Machine
     - Protocol
     - Description
   * - |image-horizon| 
     - Juno
     - India_OpenStack_Juno_
     - Native OpenStack
     - India offers a Graphical user interface to access
       OpenStack. For those interested in only managing a few images
       this may be a good way to start. The link to the GUI is 
       https://openstack-j.india.futuresystems.org/horizon . The password
       can be found by following the method discussed above.

Getting Started
-------------------------------------------------------------------------------

* Open the following URL:
  India_OpenStack_Juno_

* Use OS_USERNAME and OS_PASSWORD as a User Name and Password on Horizon.
  You can find your OS_USERNAME and OS_PASSWORD in the
  ~/.cloudmesh/clouds/india/juno/openrc.sh

.. note:: If you are using other versions of OpenStack on different cloud hosts,
          try to find your identity file with the following pattern of the path.
          $HOME/.cloudmesh/clouds/[cloud host]/[openstack version]/[openrc.sh or novarc.sh]

* Select a project that you would like to use at the project selection link at
  the top left-hand corder of the page next to the OpenStack title image.

* Choose a component that you would like to use among Compute, Network, or
  Orchestration.

The Overview page in the Compute tab shows current usage of OpenStack cloud
resources on your account.  You can also have a summary reports for a certain
period to see resource utilization, for example, how many VM instances were
being used, or how many IP addresses were allocated.

.. _India_OpenStack_Juno: https://openstack-j.india.futuresystems.org/horizon