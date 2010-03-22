require File.join(File.dirname(__FILE__), "..", "helper/spec_helper.rb")

#Include shared_examples for JSON tests
require File.join(File.dirname(__FILE__), "..", "common/json_shared.spec")


describe "The Mountain Climbing JSON API, " do

  context "when retrieving routes" do
	  before :all do
		ENV['server'] ||= 'localhost'
		@response = server_get "Routes.json"
	  end

	  it_should_behave_like "All JSON Requests"
	  it_should_behave_like "All JSON List Endpoints"      
  end


end

