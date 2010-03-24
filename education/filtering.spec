require File.join(File.dirname(__FILE__), "..", "helper/spec_helper.rb")

#Include shared_examples for JSON tests
require File.join( File.dirname(__FILE__), "..", "common/json_shared.rb")

#Include shared_examples for Education tests
require "edu_shared.rb"

describe "The Education API," do

  context "when retrieving only open schools" do
    before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "doc/schools.json?establishmentStatus.label=Open"
    end
    
    it "should only have open schools" do
      #query filters the items array to select those with just an est. label of open
       query(@response, "$.result.items[? @.establishmentStatus = 'http://education.data.gov.uk/def/school/EstablishmentStatus_Open' ]").size.should == 10
    end    
  end 

  context "when retrieving only open schools, by name of status" do
    before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "doc/schools.json?name-establishmentStatus=Open"
    end
    
    it "should only have open schools" do
      #query filters the items array to select those with just an est. label of open
       query(@response, "$.result.items[? @.establishmentStatus = 'http://education.data.gov.uk/def/school/EstablishmentStatus_Open' ]").size.should == 10
    end    
  end
      
  context "when retrieving only open schools with a nursery provision" do
    before :all do
        ENV['server'] ||= 'localhost'
        #retrieve "medium" view so we can access properties
        @response = server_get "doc/schools.json?_view=medium&establishmentStatus.label=Open&nurseryProvision=true"
    end
    
    it "should only have open schools with a nursery" do
      query(@response, "$.result.items[? @.establishmentStatus = 'http://education.data.gov.uk/def/school/EstablishmentStatus_Open' ]").size.should == 10
      query(@response, "$.result.items").each do |school|
        school["nurseryProvision"].should == true
      end      
    end    
    
  end 
  
  context "when retrieving schools with a minimum capacity" do
    before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "doc/schools.json?_view=medium&_sort=schoolCapacity&min-schoolCapacity=100&establishmentStatus.label=Open"
    end
    
    it "should respective the values in the filter" do
      query(@response, "$.result.items[? @.schoolCapacity < 100 ]").size.should == 0
      query(@response, "$.result.items[? @.schoolCapacity >= 100 ]").size.should == 10
    end
    
  end     
    
  context "when retrieving schools with a maximum capacity" do
    before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "doc/schools.json?_view=medium&_sort=schoolCapacity&max-schoolCapacity=20&establishmentStatus.label=Open"
    end
    
    it "should respective the values in the filter" do
      query(@response, "$.result.items[? @.schoolCapacity <= 20 ]").size.should == 10
      query(@response, "$.result.items[? @.schoolCapacity > 20 ]").size.should == 0
    end
    
  end  

  context "when retrieving schools with a specific capacity" do
    before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "doc/schools.json?_view=medium&_sort=schoolCapacity&schoolCapacity=5&establishmentStatus.label=Open"
    end
    
    it "should respective the values in the filter" do
      query(@response, "$.result.items[? @.schoolCapacity = 5 ]").size.should == 10
      query(@response, "$.result.items[? @.schoolCapacity > 5 ]").size.should == 0
      query(@response, "$.result.items[? @.schoolCapacity < 5 ]").size.should == 0
    end
    
  end      
end