
/*
* Flow Routes used by this project, one cluster per route
* Check this file to ensure routes are correctly set up
* and deliver the URL data desired. Group and simple routes
* are availabe for use
*/

// Home Page
FlowRouter.route('/', {
    name: 'home',
    action() {
        BlazeLayout.render("HomeLayout", {main: "Home"});
    }
});

// Dashboard Page
FlowRouter.route('/dashboard', {
    name: 'dashboard',
    action() {
        BlazeLayout.render("AppLayout", {main: "Dashboard"});
    }
});

// Profile Page
FlowRouter.route('/profile', {
    name: 'profile',
    action() {
        BlazeLayout.render("AppLayout", {main: "profile"});
    }
});

//Admin Routes
var adminRoutes = FlowRouter.group({
	prefix: '/admin',
	name: 'admin'
});
