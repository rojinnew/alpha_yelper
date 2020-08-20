#!/bin/sh

NEO4J_HOME=./neo4j-community-2.3.3
TARGET=$NEO4J_HOME/data/graph.db
SOURCE_DIR=$(realpath .)

$NEO4J_HOME/bin/neo4j-import \
    --into $TARGET \
    --multiline-fields=true \
    --id-type string \
    --nodes:Business $SOURCE_DIR/business.csv \
    --nodes:User $SOURCE_DIR/user.csv \
    --relationships:friends_with $SOURCE_DIR/friends.csv \
    --relationships:reviewed $SOURCE_DIR/review.csv \
    --relationships:tipped $SOURCE_DIR/tip.csv

$NEO4J_HOME/bin/neo4j-shell -path $TARGET -file - <<EOF
// add constraints; note that unique will also add an index to that property,
// so we don't need to do it separately
CREATE CONSTRAINT ON (u:User) ASSERT u.user_id IS UNIQUE;
CREATE CONSTRAINT ON (b:Business) ASSERT b.business_id IS UNIQUE;
CREATE CONSTRAINT ON (r:reviewed) ASSERT r.review_id IS UNIQUE;
EOF

