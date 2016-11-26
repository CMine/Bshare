//Returns boolean status of whether the current users is an admin
Template.Dashboard.helpers({
	admin: function(){
		return Roles.userIsInRole(Meteor.userId(), 'admin');
	}
});
