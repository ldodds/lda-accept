require File.join(File.dirname(__FILE__), "..", "helper/spec_helper.rb")

#Include shared_examples for JSON tests
require File.join( File.dirname(__FILE__), "..", "common/json_shared.rb")

describe "The Education API," do

  context "when accessing an unknown endpoint" do
    
    before :all do
    ENV['server'] ||= 'localhost'
    @response = server_get "fubar.json"
    end

    it "should report a 404 Not Found" do
     @response.code.should == 404       
    end
    end
  
  context "when retrieving schools" do
        before :all do
    ENV['server'] ||= 'localhost'
    @response = server_get "doc/schools.json"
    end

    it_should_behave_like "All JSON Requests"
    it_should_behave_like "All JSON List Endpoints"      

  end

  context "when retrieving primary schools" do
    
    before :all do
    ENV['server'] ||= 'localhost'
    @response = server_get "doc/schools/primary.json"
    end

    it_should_behave_like "All JSON Requests"
    it_should_behave_like "All JSON List Endpoints"      

  end

  context "when retrieving secondary schools" do
    
    before :all do
    ENV['server'] ||= 'localhost'
    @response = server_get "doc/schools/secondary.json"
    end

    it_should_behave_like "All JSON Requests"
    it_should_behave_like "All JSON List Endpoints"      

  end
        
end
