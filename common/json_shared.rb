#
# Shared examples for testing structure of JSON responses
#
shared_examples_for "All JSON Requests" do
    it "should have correct code and mimetype" do
     @response.code.should == 200
     @response.headers[:content_type].should == "application/json"       
    end

    it "should report correct format and version" do 
       query(@response, "$.format").should == "linked-data-api"
       query(@response, "$.version").should == "0.2"
    end

    it "should have a results object" do 
       query(@response, "$.result").should_not be_nil
    end

    it "should have a results object which is a hash" do 
     query(@response, "$.result").should be_an_instance_of(Hash)
    end

    it "should refer to its source" do 
     query(@response, "$.result._about").should_not be_nil
    end

    it "should refer to its API" do 
     query(@response, "$.result.isPartOf").should_not be_nil
    end

    it "should refer to its definition" do 
     query(@response, "$.result.definition").should_not be_nil
    end

end
 
shared_examples_for "All JSON List Endpoints" do 

    it "should be a list" do 
     query(@response, "$.result.type").should == "http://purl.org/linked-data/api/vocab#Page"
  end

    it "should have paging links" do 
     query(@response, "$.result.first").should_not be_nil
     query(@response, "$.result.next").should_not be_nil
    end

    it "should have page numbering" do 
     query(@response, "$.result.startIndex").should_not be_nil
     query(@response, "$.result.itemsPerPage").should_not be_nil
    end

    it "should contain some items" do 
     query(@response, "$.result.items").should_not be_empty
    end

end
