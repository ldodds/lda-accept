require File.join(File.dirname(__FILE__), "..", "helper/spec_helper.rb")

#Include shared_examples for JSON tests
require File.join( File.dirname(__FILE__), "..", "common/json_shared.rb")

#Include shared_examples for Education tests
require "edu_shared.rb"

describe "The Education API," do

 context "when increasing the page size" do
   
   before :all do
    ENV['server'] ||= 'localhost'
    @response = server_get "doc/schools.json?_pageSize=11"
   end
   
   it_should_behave_like "All JSON Requests"
   it_should_behave_like "All JSON List Endpoints"      
   
   it "should return more results" do
     query(@response, "$.result.items").size.should == 11
     query(@response, "$.result.itemsPerPage").should == "11"         
   end
      
 end
  
  context "when exceeding the maximum page size" do
    
    before :all do
     ENV['server'] ||= 'localhost'
     @response = server_get "doc/schools.json?_pageSize=1000"
    end
    
    it_should_behave_like "All JSON Requests"
    it_should_behave_like "All JSON List Endpoints"
    #this includes a check for default page size      
    it_should_behave_like "All School Requests"    
       
  end
   
end