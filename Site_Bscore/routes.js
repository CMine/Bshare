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
