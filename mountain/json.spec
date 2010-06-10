require File.join(File.dirname(__FILE__), "..", "helper/spec_helper.rb")

#Include shared_examples for JSON tests
require File.join( File.dirname(__FILE__), "..", "common/json_shared.rb")

describe "The Mountain Climbing JSON API, " do

  context "when retrieving routes" do
	  before :all do
		ENV['server'] ||= 'localhost'
		@response = server_get "Climbing/Routes.json"
	  end

	  it_should_behave_like "All JSON Requests"
	  it_should_behave_like "All JSON List Endpoints"      
  end
  
  context "when making a request to the Mountain endpoint"
    before :all do
  	ENV['server'] ||= 'localhost'
  	@response = server_get "Climbing/Mountain/Ben_Nevis.json"
    end
  
    it "should not have a language tag on properties not annotated as being api:structuredProperty" do
       query(@response, "$.result.primaryTopic.name").should_not match(/@en/)
     end

  context "when a list has no items" do
    before :all do
      ENV['server'] ||= 'localhost'
      @response = server_get "Climbing/Routes/byGrade/nosuchGrade.json"
    end
    
    it "should have an empty array under the items property" do
        query(@response, "$.result.items").should ==[]
    end
  end
  

end

